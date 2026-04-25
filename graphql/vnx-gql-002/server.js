// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-GQL-002: GraphQL query batching enabled (DoS risk)

const { ApolloServer } = require('@apollo/server');

// VULNERABLE: batching enabled without rate limiting - allows DoS via bulk operations
const server = new ApolloServer({
    typeDefs,
    resolvers,
    allowBatchedHttpRequests: true,  // Allows attackers to send many ops per request
    // Missing: no depth limit, no complexity limit, no query cost analysis
});

module.exports = server;
