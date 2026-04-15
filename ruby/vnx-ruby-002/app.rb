require "sinatra"

post "/execute" do
  code = params[:code]
  # VNX-RUBY-002: eval() with user input
  result = eval(code)
  result.to_s
end

get "/run" do
  cmd = params[:cmd]
  # VNX-RUBY-002: system() with user input
  system(cmd)
end
