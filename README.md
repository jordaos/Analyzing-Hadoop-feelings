# Analyzing Hadoop feelings
This repository aims to analyze the feelings contained in the commit messages of the Haddop project. We started with the first release of this project.

## Patterns
You need to name the analysis directories as:
- for directory no classified: `N_release_hadoop`
- for directory classified manual: `N_release_hadoop_classified_manual`
- for directory classified with Nayve Bayes: `N_release_hadoop_classified_naive_bayes`
- for directory classified with Sentistrength without filter: `N_release_hadoop_classified_ss_no_filter`
- for directory classified with Sentistrength and filter: `N_release_hadoop_classified_ss`
- for Sqlite file: `N_release_hadoo.sqlite`

*replace N with the release number. For example: the release `0.2.0` is the third release, so the value of N will be 3.

## Using Naive Bayes. Steps:

### Extract commit messages from the SQLite database to a TXT file
Run the `src/extract-commit-to-file.py` file.
Do not forget to change the location of the database in the file.

### Sort commit messages using Naive Bayes
Run the the `src/classify-with-naive-bayes-and-nltk.py` file.
You need to have a template for the algorithm to be based on. Our model is in `raw-data/1_release_hadoop_classified_manual`.

## Using SentiStrength. Steps:

### Sort commit messages
First you need to run `src/filter-wordlist.py` to filter software-specific words from SentiStrength's data files.

In order for SentiStrength to be able to parse messages, they must be in a single file, one on each line.
We filter the messages to remove links and other unnecessary information in that context.
To do this, run `src/from-sqlite-to-file-ss.py MODE RELEASE_NUMBER`, and replace `MODE` for "filter" or "no-filter" to filter or no the commit message and `RELEASE_NUMBER` for number of release that will be analised.

Now, download the SentiStrength Java tool at http://gateway.path.berkeley.edu:8080/artifactory/list/release-local/com/sentistrength/sentistrength/0.1/sentistrength-0.1.jar and move this to `data` directory.

To compute the sentiment for each commit message in the text file, go to `data` directory and run the following command:

```bash
java -jar sentistrength-0.1.jar sentidata sentistrength_data/ input ../raw-data/1_release_hadoop_ss.txt explain
```

This will generate a file with feeling points for each message.

We will convert this file to a SQLite database containing the commit punctuation and information by running the `src/convert-in-sqlite.py` file.

We now use this newly created database to classify messages as "positive," "negative," or "neutral." To do this run the file `sort-commits-sentistrength.py`.

# Verify similarity with manual classification

Run `src/verify-similarity.py MANUAL_CLASSIFICATION MODEL_CLASSIFICATION FILE_NAME`

- To preview results for first analysis, go to https://goo.gl/kJVj6V