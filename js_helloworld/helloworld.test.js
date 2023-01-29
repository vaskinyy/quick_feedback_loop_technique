const hello = require('./helloworld')

test('returns hello world', () => {
    expect(hello.output()).toBe('Hello World');
});
