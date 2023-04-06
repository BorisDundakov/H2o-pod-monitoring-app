import time, datetime
from h2o_wave import site, ui, data
import psutil


def bytes_to_kb(b):
    return int(b*0.001)


page = site['/']

cpu_card = page.add('cpu_stats', ui.small_series_stat_card(
    box='1 1 2 2',
    title='CPU',
    value='={{usage}}%',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$red',
))

core_card = page.add('cpu_cores', ui.small_series_stat_card(
    box='3 1 2 2',
    title='CPU Cores',
    value='={{usage}}',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$purple',
))

mem_card = page.add('mem_stats', ui.small_series_stat_card(
    box='1 3 2 2',
    title='Memory',
    value='={{usage}}%',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$blue',
))

disk_usage_card = page.add('disk_usage_stats', ui.small_series_stat_card(
    box='3 3 2 2',
    title='Disk usage',
    value='={{usage}} %',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$pink',
))

network_io_sent_card = page.add('io_sent_card', ui.small_series_stat_card(
    box='3 5 2 2',
    title='Network Bytes Sent',
    value='={{usage}} KB',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$yellow',
))


boot_card = page.add('boot_stats', ui.small_series_stat_card(
    box='3 7 2 2',
    title='Last Boot',
    value='={{usage}}',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$cyan',
))

network_io_received_card = page.add('io_received_card', ui.small_series_stat_card(
    box='1 5 2 2',
    title='Network Bytes Received',
    value='={{usage}} KB',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$yellow',

 ))

rss_card = page.add('rss_card', ui.small_series_stat_card(
    box='1 7 2 2',
    title='Process rss',
    value='={{usage}} KB',
    data=dict(upload_speed=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$green',

))

tick = 0

while True:
    tick += 1

    cpu_usage = psutil.cpu_percent(interval=1)   # <--- CPU utilization in percentage measured inside the pod
    cpu_card.data.usage = cpu_usage
    cpu_card.plot_data[-1] = [tick, cpu_usage]

    mem_usage = psutil.virtual_memory().percent
    mem_card.data.usage = mem_usage              # <--- available memory in the pod
    mem_card.plot_data[-1] = [tick, mem_usage]

    cpu_count = psutil.cpu_count()               # <-- total number of available cpu cores 
    core_card.data.usage = cpu_count
    core_card.plot_data[-1] = [tick, cpu_count]

    disk_usage = psutil.disk_usage('/')  # requires a path
    disk_value = f"{disk_usage.percent:.2f}"
    disk_usage_card.data.usage = disk_value
    disk_usage_card.plot_data[-1] = [tick, disk_usage.percent]

    network_io_bytes_sent = psutil.net_io_counters().bytes_sent
    kb_sent = bytes_to_kb(network_io_bytes_sent)
    network_io_sent_card.data.usage = kb_sent
    network_io_sent_card.plot_data[-1] = [tick, kb_sent]

    network_io_bytes_received = psutil.net_io_counters().bytes_recv
    kb_received = bytes_to_kb(network_io_bytes_received)
    network_io_received_card.data.usage = kb_received
    network_io_received_card.plot_data[-1] = [tick, kb_received]

    boot_time = psutil.boot_time()
    bt = (datetime.datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S"))
    boot_card.data.usage = bt
    boot_card.plot_data[-1] = [tick, boot_time]

    current_process = psutil.Process()
    memory_info = current_process.memory_info().rss
    rss_card.data.usage = memory_info
    rss_card.plot_data[-1] = [tick, memory_info]

    page.save()
    time.sleep(1)
