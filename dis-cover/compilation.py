import subprocess

def compile_under_scenario(source_file_name, scenario, output_directory):
    (compiler, option) = scenario
    output_file_name = "%s/%s_%s_%s" % (output_directory, source_file_name.split("/")[-1][:-4], compiler, option[1:])
    command = [compiler, "-pie", "-fPIC", "-fPIE", option , source_file_name, "-o", output_file_name]
    print("Running compilation : %s" % " ".join(command))
    process = subprocess.run(command)
    if process.returncode == 0:
        return output_file_name
