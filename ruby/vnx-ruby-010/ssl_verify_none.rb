# vnx-ruby-010 eval target
require 'openssl'
require 'net/https'

# TRIGGERS: VERIFY_NONE disables TLS certificate validation
def fetch_url_insecure(url)
  uri = URI.parse(url)
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_NONE
  http.get(uri.request_uri)
end

# TRIGGERS: VERIFY_NONE in SSL context
def create_insecure_ssl_context
  ctx = OpenSSL::SSL::SSLContext.new
  ctx.verify_mode = OpenSSL::SSL::VERIFY_NONE
  ctx
end

# Safe alternative:
# http.verify_mode = OpenSSL::SSL::VERIFY_PEER
# http.ca_file = '/etc/ssl/certs/ca-certificates.crt'
