# VNX-RUBY-003: Insecure deserialization
data = File.read("user_data.bin")
obj = Marshal.load(data)
puts obj.inspect
