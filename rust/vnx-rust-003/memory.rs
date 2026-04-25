// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-RUST-003: Rust unsafe block

use std::ptr;

pub fn read_raw_memory(ptr: *const u8, len: usize) -> Vec<u8> {
    let mut result = Vec::with_capacity(len);

    // VULNERABLE: unsafe block with raw pointer arithmetic
    unsafe {
        for i in 0..len {
            result.push(*ptr.add(i));
        }
    }
    result
}

// VULNERABLE: unsafe function declaration
pub unsafe fn write_to_pointer(dst: *mut u8, value: u8) {
    ptr::write(dst, value);
}

pub fn process_buffer(data: &[u8]) -> u32 {
    // VULNERABLE: unsafe transmute
    unsafe {
        let ptr = data.as_ptr() as *const u32;
        *ptr
    }
}
