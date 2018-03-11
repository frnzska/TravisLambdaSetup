# TravisLambdaSetup

Example project to deploy lambda function code with Travis-Ci to s3 as zips, includes tests to mock AWS resources.

Structure:
<pre>
- lambda_fct:
            - src
            - tests
            - specs
            - requirements.txt
- .travis.yml
- travis # with packaging script
</pre>