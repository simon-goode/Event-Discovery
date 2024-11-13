# Event-Discovery
Event Discovery Coding Challenge for Shmooze.

### Summary
Accepts input data as JSON with tags for target audience, key goals, and other business goals for an industry event. Outputs (as JSON file) a top 10 list of the most relevant industry events from 10times.com.

### Assumptions

Input file is JSON with following structure:
```json
{
    "target": "target audience",
    "objectives": "key goals for event participation",
    "industry": "one of [education-training, finance, building-construction, wellness-healthcare, food-beverage, electronics-electricals, fashion-accessories, travel-tourism, telecommunication, hospitality, medical-pharma, business-consultancy, entertainment, power-energy, arts-crafts, logistics-transportation, trade-promotion, apparel-fashion, animals-pets, packaging, technology, engineering, research, agriculture-forestry, waste-management, automotive, home-office, security, baby-kids]",
    "location": "geographic region or city",
    "budget": "cost-to-enter budget",
    "KPIs": "relevant metrics or outcomes that the marketer aims to achieve from the event"
  }
  ```
An example input file is included in the src directory.

The output JSON file will contain a list of events, with Event Name, Event URL, Event Description, and Request-Matching Score taglined. An example output file is included in the src directory.

### Improvements
Because this implementation uses slow web scraping and OpenAI API calls, it takes ~15 seconds to run. Speed (and quality of results) could likely be improved with calls to a dedicated industry event API like PredictHQ or BizProspex Events API.