# vnx-ruby-008 eval target
require 'open3'

# TRIGGERS: Open3.pipeline with dynamic command from user input
def run_pipeline(user_command)
  Open3.pipeline(user_command)
end

# TRIGGERS: Open3.pipeline_r with variable argument
def process_data(input_cmd, output_cmd)
  Open3.pipeline_r(input_cmd, output_cmd) do |stdin, stdout, wait_threads|
    stdout.read
  end
end

# TRIGGERS: Open3.pipeline_rw with interpolated command
def convert_file(filename)
  Open3.pipeline_rw("cat #{filename}", "grep ERROR")
end

# Safe alternative: use array form with fixed commands
# Open3.pipeline(["convert", "-resize", "100x100", input_file, output_file])
