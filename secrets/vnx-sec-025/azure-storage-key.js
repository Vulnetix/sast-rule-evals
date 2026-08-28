// vnx-sec-025 eval target: Azure Storage Account key hardcoded
//
// VNX-SEC-025 needs two things on one line: an identifier matching
// azure[_-.]?(storage)?[_-.]?(account)?[_-.]?key, and a run of 86 base64
// characters followed by '=='. It does NOT need an Azure connection string,
// and this fixture deliberately omits one: a DefaultEndpointsProtocol/
// AccountKey wrapper is what GitHub's push-protection scanner matches on, so
// including it made the fixture unpushable while adding nothing to the test.
//
// The value below is 86 characters of repeated "NOTAREALKEY" plus '==', which
// satisfies the rule's shape and is self-evidently not a credential.
const azure_storage_account_key = "NOTAREALKEYNOTAREALKEYNOTAREALKEYNOTAREALKEYNOTAREALKEYNOTAREALKEYNOTAREALKEYNOTAREALK==";  // TRIGGERS rule
