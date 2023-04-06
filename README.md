# H2o Pod monitoring application

![Screenshot from 2023-04-06 12-39-36](https://user-images.githubusercontent.com/71731579/230340281-0d8c63a0-310e-410d-a866-6f0a3824ea69.png)

Monitor your pod performance in a Kubernetes cluster using the h2o-wave-app library!

## Future maintenance

Bear in mind that the h2o wave application needs specific version of the libraries specified in the 'requirements.txt' file located inside 'h2o_wave_app' folder. Dependabot github security updates will keep your application secure, as long as it is regularly updated in your own github repository. The libraries inside 'requirements.txt' are dependent of each other, so changing the version of one library may break the entire application. Therefore it is recommended to update the libraries to their latest version and test by building the image locally first. Feel free to change the image inside your deployment to one that satisfies the purpose and needs of your own project.



## References
- Kubernetes docs: https://kubernetes.io/docs/concepts/architecture/

- H2o wave library: https://wave.h2o.ai/

- H2o app reference guide: https://github.com/srini-x/wave-heroku

- H2o system monitor tutorial: https://wave.h2o.ai/docs/tutorial-monitor
