# Timeline of the bitcoin development history

This open source project contains the data for a timeline on historical Bitcoin developments.

> To fully understand the current Bitcoin protocol development, knowledge about historical events is essential. 

Feel free to propose a change or a new entry to the timeline. 
All code in this repository is licensed under a MIT License.
The data contained in the `bitcoin-history.json` file is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>


A example usage can be found in this [blog post](https://b10c.me/The-incomplete-history-of-Bitcoin-development/).

Most points on the timeline are adopted from a talk [John Newbery](https://twitter.com/jfnewbery) gave on the [History and Philosophy of Bitcoin Development](https://www.meetup.com/BitDevsNYC/events/262321510/). 

## Formatting

The `bitcoin-history.json` file contains a sorted list of events on the timeline. It starts with Satoshi Nakamoto beginning his work on Bitcoin in 2007. Each event is encoded in the following JSON structure. Correct formatting can be checked with the Python script `json-format-checker.py`. This script is automatically run for each pull request on travis. 

An `id` must start with a year and a valid type.
Currently the five `types` release, post, bug, company and other are specified.
The `title` should contain a date a column as separator and a short title. 
At least one `paragraph` must be filled. No empty paragraphs.
`Links` to a source should be provided. Each `link` must have an according `label`. 

```json
{
  "id": "",
  "type":"",
  "title": "",
  "paragraphs": [
    ""
  ],
  "links": [
    {
      "label": "",
      "link": ""
    }
  ]
}
```
