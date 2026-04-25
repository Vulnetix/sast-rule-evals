# VNX-RUBY-004: SQL injection
class UserController < ApplicationController
  def show
    user = User.find_by_sql("SELECT * FROM users WHERE name = '#{params[:name]}'")
    render json: user
  end
end
