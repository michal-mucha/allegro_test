import re
import sys

if __name__ == "__main__":
    docker_file_template_path = sys.argv[1]
    path_of_final_docker_file = sys.argv[2]
    service_name = sys.argv[3]
    if service_name is None or docker_file_template_path is None or path_of_final_docker_file is None:
        raise Exception("Required arguments not passed. Provide arguments in proper order and try again")

    print(f'Creating of Dockerfile for service: {service_name} started')
    final_docker_file_content = []
    service_pointer_pattern = '{{service_name_pointer}}'
    print(f'Reading Dockerfile from path: {docker_file_template_path}')
    with open(docker_file_template_path, "r") as dockerfile_content:
        for line in dockerfile_content.readlines():
            if re.search(service_pointer_pattern, line) is not None:
                line_with_pointer_replaced = re.sub(service_pointer_pattern, f'{service_name}.dll', line)
                final_docker_file_content.append(line_with_pointer_replaced)
                continue
            final_docker_file_content.append(line)

    print(f'Writing Docker file to {path_of_final_docker_file}')
    with open(path_of_final_docker_file, 'w') as docker_file:
        docker_file.write("".join(final_docker_file_content))
