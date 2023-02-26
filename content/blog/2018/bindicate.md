---
date: 2018-06-29T06:00:00+06:00
lastmod: 2018-06-29T17:30:00+06:00
title: "Bindicator - an Alexa skill for bin collections"
authors: ["david"]
categories:
  - blog
tags:
  - computing
slug: bindicate
---

{{% epigraph  %}}
A Glasgow-based IT consultant who developed a little bin-shaped device that lights-up with different colours to indicate which bins are due for collection prompted me to do something similar with Alexa and AWS lambdas. It’s essentially free, and free is good.
{{% /epigraph  %}}


# Introduction # 

Can’t remember which bins to put out? This is a quick look at an Alexa skill I’ve developed that uses my local council’s website as a source of information about bin collections, and lets me ask Alexa when my next bin collection is, and what bins are being collected, and when any particular bin is next being collected. Like this:

+ *‘**Alexa** bindicate next*
+ *‘**Alexa** bindate all‘*
+ *‘**Alexa** bindicate recyclable‘*
+ *‘**Alexa** bindicate green‘*


#### Tech involved ####
Among the ever-growing offering of Amazon Web Services (AWS) is the serverless function called a lambda, a function in the cloud that runs without you needing to bother with server instances. I’ve written two lambdas for this job:

* one lambda to collect and store the bin collection data
* another lambda to serve up that data in a friendly form to an Alexa skill.

and I’m storing the data in an AWS S3 bucket - Amazon’s low-cost object storage solution.

#### Cost #### 

Lambdas and S3 are inexpensive. Cloud computing costs are notoriously difficult to estimate – and I wouldn’t be at all surprised if that opaqueness wasn’t deliberate. But here are a few back-of-the-envelope calculations.

{{% fagpacket %}}

#### Costs ####

* **Lambdas** - the AWS free tier gives you 1 million requests per month, and 400,000 GB-seconds of compute time per month. After that, they cost $0.02 per 1,000,000 requests.
* **S3 storage** - $0.0125 or $0.023 per GB, depending on access frequency; and £0.001 per 1,000 PUT requests, $0.001 per 10,000 GET requests (low access frequency)

My usage will be storing one JSON file in S3 of just a few bytes; and PUTting at maximum 31 x 24 times per month, GETting 2 x 31 times per month. The lambda to do the retrieval and storing will be run, at most, hourly; the lambda to service the Alexa skill will be called, realistically, a couple of times per day, max. We’re dealing with vanishingly small costs here.

{{% /fagpacket %}}



## Development Languages ##
AWS lambdas can be written natively in Node, Python, Java, C# and Go.

Now, when a lambda is called for the first time there’s a slight delay as it starts up, and that delay is greater with Java, C# and Go than with Node and Python. If the lambda is subsequently kept ‘warmed-up’ by being repeatedly and frequently called, this will be a one-off time cost. But in my case, the first lambda that does the data collection will be run hourly at most, and I can’t see myself calling the Alexa skill any more frequently – while I think it might be useful, I don’t think I’ll want to be told several times a day when the bins are due –so this startup time will be a repeated burden on processing, which would make itself apparent in a very slow response from Alexa. For that reason I’ve used Python scripts for the Alexa skill lambda and for the other one too.




## The Data ## 
Where to get the data?

I don’t know if my local council offers a structured feed of bin collection data – I might have a look around to see if there’s an RSS or a JSON feed – but I already know it has a web page that, on entering a postcode, gives me a URL that hosts all the services information I need. That’s pretty useful and a few years ago would have been highly unusual for local authorities, who seemed to be vying with each other to create the most unusable website. But now, with this website, it’s a simple matter to read it using Python, parse out the bin collection data I need, and store it somewhere – I’m storing it because I don’t want to hit the council’s website every time someone asks Alexa for the bin collection details. It doesn’t really matter for my own use but you could imagine such a service being used by many people, on many council websites, and I’d like to be a good player here, seeing that the council have had the sense to provide the data in the first place. So instead I’m saving the bin collection information, infrequently but regularly, in a structured, easy-to-retrieve store.

The page on the local council website has a section that looks like this:


{{< figure src="https://c2.staticflickr.com/2/1805/41994658415_0fd0fdbb9d.jpg"  
link="https://c2.staticflickr.com/2/1805/41994658415_0fd0fdbb9d.jpg"  
 class="figimg"
>}}

and the underlying markup is clean and straightforward (well done, local council):


{{< highlight html >}}
<ul>

    <li>Your next Garden Waste collection is on <strong>27/06/2018</strong></li>

    <li>Your next Recycling collection is on <strong>27/06/2018</strong></li>

    <li>Your next Domestic Waste collection is on <strong>20/06/2018</strong></li>

</ul>
{{< /highlight  >}}


…and that’s pretty easy to parse, given that the HTML patterns don’t appear anywhere else in the page.

The disadvantage of using this page-scraping method instead of a dedicated, structured feed is that the local authority could decide to change their page in a way that spoils my parsing, or change the structure of the website to remove the URL. A later refinement for my lambda would be to add some logging and alerting in case of a failure to read the page or to the parse data we expect to always be present.


## AWS lambda #1: collecting the data ##

The nuts and bolts of the data collection is a simple bit of python code that reads in the URL of the council’s bin collection page for my postcode and parses out the data.

In Python, that’s something like this:

{{< highlight python >}}

try:
    response = urllib.request.urlopen(‘http://{my council URL}‘)
    page = response.read().strip()
    return(page)
except:
    return None;
{{< /highlight  >}}


and there are a number of choices for parsing the data. I’ve gone with regex because I always forget regex patterns so any opportunity to remind myself about them is generally useful. Regex reminds me of Kurt Vonnegut’s description of the US National Anthem - gibberish sprinkled with question marks. That’s regex but you have to admit it’s very useful sometimes.

Setting up a lambda in AWS is straightforward. Log into - or create - your developer account here:

https://aws.amazon.com/console/



and then from the bewildering lists of possibilities, choose ‘Lambda’. Go right ahead and create a new ‘function’ as the lambdas are suddenly called once you get into this area.

You can type - or better still, cut-and-paste – your python code directly into the code editing aread you see in front of you. You’ll want to import:




{{< highlight python >}}
import json
import boto3
{{< /highlight  >}}

– boto3 is the library used by Python to access S3. Remember, once we’ve read the web page and parsed out the data, we want to store it as JSON into S3.

I start by setting-up a JSON structure that looks like this:



{{< highlight json >}}
bins = {
    "Domestic": {
      "colour": "Grey",
      "description": "Domestic waste",
      "keystring" : '<li>Your next <strong>Domestic Waste',
        },
    "Garden" : {
      "colour": "Green",
      "description": "Garden waste",
      "keystring" : "<li>Your next <strong>Garden Waste",
    },
    "Recycling": {
      "colour": "Brown",
      "description": "Recycling waste",
      "keystring" : '<li>Your next <strong>Recycling',
    }
  }
{{< /highlight  >}}

and after successfully reading in the council’s website I add another property, the next collection date, to each of these nodes.

## Storing in S3 ##
I use the boto package to access the storage option, AWS S3.

S3 is simple, low-cost object storage that’s ideal for the job here, of saving (structured) JSON. You’ll need to create what AWS calls a ‘bucket’ and give it a name - I’ve called mine, ‘bincollection’.

Be careful with access permissions here. You do not want the rest of the world to be able to access your data. Only your two lambdas should have access - one to write and overwrite the JSON file, the other to read it.

And talking of permissions: here’s a reminder that your lambda will need to run under a USER that has a ROLE that allows S3 access.

{{< highlight python >}}


def getCollectionFromBucket():
    S3_BUCKET_NAME = "bincollection"
    keyname = "{your unique key}"
    s3 = boto3.resource("s3")
    obj = s3.Object(S3_BUCKET_NAME,keyname)
    
    content_object = s3.Object(S3_BUCKET_NAME, keyname)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    return json.loads(file_content)
{{< /highlight  >}}



## AWS lambda #2: retrieving the data and telling Alexa
Alexa programs, processes, applications – call them what you will – are know as Skills, and an Alexa Skill is a voice-interface to a lambda. It’s the AWS lambda that does all the work and formulates the response for Alexa.

So the second lambda reads the content out of the S3 bucket - using boto again:
{{< highlight python >}}
def getCollectionFromBucket():
    S3_BUCKET_NAME = "bincollection"
    keyname = "{your unique key}"
    s3 = boto3.resource("s3")
    obj = s3.Object(S3_BUCKET_NAME,keyname)
    content_object = s3.Object(S3_BUCKET_NAME, keyname)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    return json.loads(file_content)

def getBinCollectionResponse():
  try:
        bins = getCollectionFromBucket()
        for(key, value) in bins.items():
           :
           :
           {build your speech response}
            speech_output = speech_output + " " + value["description"] + " "  + value["nextCollectionDate"]+ ". "
        return speech_output
    except:
        speech_output = "an error occurred"
{{< /highlight  >}}

Again, this lambda needs user-role access to S3: and it also needs to handle the incoming text from Alexa. If you’ve never created an Alexa skill before I’d advise using an existing Alexa template sample, and cannibalising it. Get it working with a simple command first and then expand on it.

## The Alexa Skill ##

To create the Alexa Skill you’ll use the Alexa Skills Kit Developer Console,

https://developer.amazon.com/alexa/console/ask

Give your skill a unique name, select ‘Custom’ on the next page, and create the skill.

This blogpost isn’t going to take you through the details of crating a skill. There are plenty of blogposts and AWS documents out there but things to bear in mind:

* You need to define an invocation - the key word or words that you use to wake Alexa up and respond to you
* You’ll need to define intents - an action you’ll take, with one or more sets of keywords or phrases to kick-off that action
* And don’t forget the endpoint - this is where you paste the URN of the lambda you just created, the one that services the Alexa requests. You’ll find it at the top-right of the Lambda editing page.

## And that’s it ##
I was surprised by Alexa, and how quickly I took to using voice commands. Part of that, I’m sure, is the personality of Alexa - in contrast, say, to Google Home. A challenge for me and any of you who try this is to make the speech responses seem natural and idiomatic.