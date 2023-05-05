# Password Cracking - JWT
Category: Password Cracking

## Description
I hope you like our new blog!

For no apparent reason, it has an admin page with the flag you're after.

## Write-up
- The current user's session token can be retrieved from the browser developer tool. The token is a JWT token: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc19hZG1pbiI6ZmFsc2V9.-ludxzXK6MiqPloJBLV1grY4_qtsw0cbvzVsicqSn2g`.
- Decoding the token reveals the payload: `{ "is_admin": false }`.
- To escalate privileges, we can modify the boolean value of `is_admin` to true.
- Additionally, the signature of the token needs to be updated accordingly.
- After conducting analysis with John The Ripper, the signature key was discovered to be `zebralicious`.
- The forged token becomes: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc19hZG1pbiI6dHJ1ZX0.A4Juso7QJbPQiaOs_w2rscAlzIJLva0KlK0UZLua0Gw`.
- By accessing the `/admin` endpoint with the forged token, the flag is presented.

Flag: `punk_{F5OJNLLSPIBASVD8}`
