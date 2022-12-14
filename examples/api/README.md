# VuePilot API Documentation & Examples

This repository is for reference when working the VuePilot API.

You will find various examples for common use cases when interacting with the VuePilot API along with general documentation here.

This is a work in progress repo and will be added to gradually over time depending on customer demand

## API Responses

All API responses are in JSON format

## Authentication

The VuePilot API can be authenticated to via standard HTTP Authorization headers and by use of `Bearer` tokens.

API keys are issued per user and are available from the `Profile` section of the dashboard found at: https://www.vuepilot.com/users/edit

## Example

The example below will return a listing of apps in your account using basic cURL.

```
curl -H "Authorization: Bearer <your token>" https://www.vuepilot.com/api/v1/apps
```
