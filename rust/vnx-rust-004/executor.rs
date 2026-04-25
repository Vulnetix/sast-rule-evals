// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-RUST-004: Rust command injection via process::Command with format!

use std::process::Command;

pub fn run_tool(user_input: &str) {
    // VULNERABLE: user input interpolated into command via format!
    let cmd = format!("mytool {}", user_input);
    Command::new(cmd).output().expect("Failed to execute");
}

pub fn convert_file(filename: &str) {
    // VULNERABLE: format! used to construct command with user-controlled filename
    Command::new(format!("convert {}", filename))
        .output()
        .unwrap();
}

pub fn run_shell_command(args: &str) {
    // VULNERABLE: shell interpreter invoked with user-controlled content
    Command::new("sh")
        .arg("-c")
        .arg(args)
        .output()
        .expect("Failed to execute command");
}
