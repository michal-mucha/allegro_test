import re
import sys

if __name__ == "__main__":
    docker_file_template_path = sys.argv[1]
    path_of_final_docker_file = sys.argv[2]
    service_name = sys.argv[3]
    if service_name is None or docker_file_template_path is None or path_of_final_docker_file is None:
        raise Exception("Required arguments not passed")
    final_docker_file_content = []
    service_pointer_pattern = '{{service_name_pointer}}'
    with open(docker_file_template_path, "r") as dockerfile_content:
        for line in dockerfile_content.readlines():
            if re.search(service_pointer_pattern, line) is not None:
                line_with_pointer_replaced = re.sub(service_pointer_pattern, service_name, line)
                final_docker_file_content.append(line_with_pointer_replaced)
                continue
            final_docker_file_content.append(line)

    with open(path_of_final_docker_file, 'w') as docker_file:
        docker_file.write("\n".join(final_docker_file_content))