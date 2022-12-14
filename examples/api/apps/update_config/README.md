# Updating App Config

You may wish to programmatically update an apps configuration, for example changing the text on an announcement app or updating the video URL on a video app.

We can do this this with a simple script, but first we need to get a copy of the original apps configuration that we will modify and send back to the API. All apps have different config options with different keys. These keys may also change over time so it is recommended to update the source config often rather than storing a static copy locally.

**IMPORTANT** When updating app configuration you must send back the `FULL APP CONFIGURATION`, not just the attributes you wish to change. This is why we use the `**` operator in the scripts, to include all the other properties

As an example, this is what a full configuration for an announcement app looks like.

```
{
  "id": 1113,
  "name": "Mask Announcement",
  "token": "a001aba5",
  "category": "announcement",
  "url": "https://www.vuepilot.com/app/a001aba5-344",
  "config": {
    "align_items": "bottom",
    "bg_type": "random_image",
    "bg_color": "#64798D",
    "bg_size": "cover",
    "bg_position": "center center",
    "font_weight": "normal",
    "text": "Please Wear A Mask When Indoors",
    "keywords": "covid mask",
    "text_color": "#ffffff",
    "url": "https://images.unsplash.com/photo-1584634731339-252c581abfc5",
    "show_text_backing": true
  },
  "content": null
}
```

We can update just the option for `text` in the `config` block and send back the whole payload using

`new_config = {**result, 'config': {**result["config"], 'text': UPDATED_TEXT}}`

## Retrieve Current App Config

To see the configuration for your app, get the apps unique token from the apps edit URL (its the 8 alpha numeric letters at the end) and perform a cURL to the app show endpoint (piping to `jq` for terminal JSON formatting is recommended but not required)

```
curl -H "Authorization: Bearer <your token>" https://www.vuepilot.com/api/v1/apps/<token> | jq
```

Now that we know the shape of the apps configuration, we can write the script to pull down the app config, then update the attributes we need and send it back. This will ensure that any new attributes that have been added over time are also included.

## Usage

Edit the script for your use case, in our example we are updating the text on an announcement app.

Update the `APP_TOKEN` and `UPDATED_TEXT` variables at the top of the script file then run the script

```
python update_config.py
```

**Output**

```
App updated successfully
URL: https://www.vuepilot.com/dashboard#/apps/announcement/a001aba5
```
