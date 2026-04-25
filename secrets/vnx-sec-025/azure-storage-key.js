// vnx-sec-025 eval target: Azure Storage Account key hardcoded
const azureStorageAccountKey = "DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=dGVzdGtleXZhbHVlZm9yZXZhbHRhcmdldHRlc3RpbmcxMjM0NTY3ODkwYWJjZGVmZ2hpamtsbW5vcHFyc3Q==;EndpointSuffix=core.windows.net";  // TRIGGERS rule

// Connection config with key pattern
const storageConfig = {
    azure_storage_account_key: "dGVzdGtleXZhbHVlZm9yZXZhbHRhcmdldHRlc3RpbmcxMjM0NTY3ODkwYWJjZGVmZ2hpamtsbW5vcHFyc3Q==",  // TRIGGERS rule
};
