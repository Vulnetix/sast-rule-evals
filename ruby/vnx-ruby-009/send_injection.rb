# vnx-ruby-009 eval target

class UsersController < ApplicationController
  # TRIGGERS: send with params-derived method name
  def update
    method_name = params[:action_type]
    @user.send(method_name, params[:value])
  end

  # TRIGGERS: public_send with request-derived method
  def dispatch
    @resource.public_send(request.params[:method])
  end

  # TRIGGERS: __send__ with params
  def call_method
    result = SomeService.__send__(params[:service_method], params[:arg])
    render json: result
  end
end

# Safe alternative: use an explicit allowlist
# ALLOWED_METHODS = %w[activate deactivate suspend].freeze
# if ALLOWED_METHODS.include?(method_name)
#   @user.public_send(method_name)
# end
