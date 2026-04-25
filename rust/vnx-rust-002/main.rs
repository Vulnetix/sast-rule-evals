// VNX-RUST-002: unwrap may panic
use std::fs;

fn main() {
    let content = fs::read_to_string("config.toml").unwrap();
    let port: u16 = content.lines().next().expect("no first line").parse().unwrap();
    println!("Port: {}", port);
}
