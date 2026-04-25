// vnx-gql-004 eval target: GraphQL field suggestions not disabled
const { ApolloServer } = require('@apollo/server');

// TRIGGERS rule: ApolloServer without suggestions: false
const server = new ApolloServer({  // TRIGGERS rule
    typeDefs,
    resolvers,
    // suggestions: false  <-- not set, leaks schema field names in errors
});

// TRIGGERS rule: graphql-yoga without maskedErrors
const { createYoga } = require('graphql-yoga');
const yoga = createYoga({  // TRIGGERS rule
    schema,
    // maskedErrors: true  <-- not set
});
