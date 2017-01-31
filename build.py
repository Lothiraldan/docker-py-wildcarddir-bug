from docker import DockerClient

DOCKER = DockerClient()

stream = DOCKER.api.build('.', stream=True, decode=True)
for log_line in stream:
    if log_line:
        print(log_line.get('stream'), end="")
