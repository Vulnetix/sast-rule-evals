# VNX-RUBY-006: Mass assignment
class UsersController < ApplicationController
  def create
    @user = User.create(params)
    redirect_to @user
  end
end
