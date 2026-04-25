// vnx-gql-003 eval target: GraphQL query string injection
const { graphql } = require('graphql');

// TRIGGERS rule: user input interpolated into GraphQL operation string
app.post('/api/search', async (req, res) => {
    const fragment = req.body.fragment;
    const query = `query { user { ${fragment} } }`;  // TRIGGERS rule
    const result = await graphql({ schema, source: query });
    res.json(result);
});

// TRIGGERS rule: concatenation
app.post('/proxy', async (req, res) => {
    const userFields = req.query.fields;
    const mutation = "mutation { updateUser { " + userFields + " } }";  // TRIGGERS rule
    await fetch('/graphql', { method: 'POST', body: JSON.stringify({ query: mutation }) });
});
