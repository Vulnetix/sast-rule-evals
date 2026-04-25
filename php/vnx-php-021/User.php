<?php
// Triggers VNX-PHP-021: Laravel mass assignment via empty guarded array
namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    // UNSAFE: $guarded = [] disables all mass-assignment protection
    // An attacker can set any field including is_admin, role, password_hash
    protected $guarded = [];
}

class Post extends Model
{
    // Also triggering: Model::unguard() in a service provider would disable
    // mass assignment globally. Here we show the per-model pattern.
    protected $guarded = [];
}
