# Create Rotation With Bulk URLs From CSV

You may wish to create a rotation made up of a large number of URLs. This would be a pain to do manually one by one so we can use a simple script to perform this creation of this rotation.

In this example we will show you how to read in simple URLs from a CSV which can be crafted using any spreadsheet program and then by using a Python script, create a rotation and supply a listing of "pages", taken from the CSV to add to the rotation.

The `pages.csv` is loaded by the `create_rotation.py` script, converted into JSON and a structured payload is then POSTed to the API which creates the rotation.

**PLEASE NOTE** This script is used for creating new rotations only, it does not update an existing rotation.
That is a different task and requires mapping the internal IDs to each page so they aren't duplicated.

Once created, you can manage the rotation directly from the dashboard

## Usage

Update the URLs in the `pages.csv` accordingly then run

```
python create_rotation.py
```

**Output**

```
Rotation created successfully
URL: https://www.vuepilot.com/dashboard#/rotations/45753
```
