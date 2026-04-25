// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-RUST-006: integer truncation/sign-change cast after parsing

fn process_port(s: &str) {
    // TRIGGERS VNX-RUST-006: parse to i64 then cast down to i16 - silently truncates large values
    let port: i64 = s.parse::<i64>().unwrap_or(0);
    let small_port = port as i16;
    println!("Port: {}", small_port);
}

fn compute_index(s: &str) -> u8 {
    // TRIGGERS VNX-RUST-006: usize cast to u8 - values > 255 silently wrap
    let n: usize = s.parse().unwrap_or(0);
    n as u8
}

fn convert_offset(raw: usize) -> i32 {
    // TRIGGERS VNX-RUST-006: usize (unsigned) cast to i32 (signed) - may produce negative value
    raw as i32
}
