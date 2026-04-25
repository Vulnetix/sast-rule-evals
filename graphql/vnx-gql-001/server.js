// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-GQL-001: GraphQL introspection enabled in production

const { ApolloServer } = require('@apollo/server');
const { graphqlHTTP } = require('express-graphql');

// VULNERABLE: introspection enabled - exposes entire schema to attackers
const server = new ApolloServer({
    typeDefs,
    resolvers,
    introspection: true,  // Should be false in production
});

// VULNERABLE: GraphiQL IDE enabled in production
const graphqlMiddleware = graphqlHTTP({
    schema: schema,
    graphiql: true,  // Should be false in production
    rootValue: resolvers,
});

module.exports = { server, graphqlMiddleware };
