# vnx-ruby-007 eval target
require 'yaml'

# TRIGGERS: YAML.load() with arbitrary input can execute Ruby code
def parse_config_bad(yaml_string)
  YAML.load(yaml_string)
end

# TRIGGERS: YAML.load() from user-supplied request body
def parse_user_data(request_body)
  data = YAML.load(request_body)
  data
end

# Safe alternative:
# YAML.safe_load(yaml_string)
# Psych.safe_load(yaml_string, permitted_classes: [Symbol])
