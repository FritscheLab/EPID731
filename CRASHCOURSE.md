# EPID731 Crash Course

## Repository Mapping

The EPID731 repository is organized into folders for **Day 2** and **Day 4**, along with supporting files. The table below summarizes each top-level folder/file, its role in the workshop, and key notebooks or scripts:

| Folder/File | Role in Workshop                                                                                               | Key Content (Notebooks/Scripts)                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Day2/`     | Day 2 materials focusing on accessing & analyzing EHR data with **R**.                                         | **Jupyter Notebooks:** [EPID731\_Accessing\_EHR\_Data.ipynb](https://colab.research.google.com/github/FritscheLab/EPID731/blob/main/Day2/EPID731_Accessing_EHR_Data.ipynb) (main Day 2 notebook), [EPID731\_BonusWhiteRabbit.ipynb](https://colab.research.google.com/github/FritscheLab/EPID731/blob/main/Day2/EPID731_BonusWhiteRabbit.ipynb) (optional White Rabbit tutorial).                                                            |
| `Day4/`     | Day 4 materials focusing on harmonizing medication data with **GPT** models (using OpenAI API via **Python**). | **Notebook:** [EPID731\_Medication\_Classification\_with\_OpenAI\_GPT\_API.ipynb](https://colab.research.google.com/github/FritscheLab/EPID731/blob/main/Day4/EPID731_Medication_Classification_with_OpenAI_GPT_API.ipynb) (main Day 4 tutorial); **Subfolders:** `configs/` (example configuration `.ini` files), `inputs/` (sample input data files), `prompts/` (GPT prompt templates), `scripts/` (Python scripts for batch processing). |
| `README.md` | Repository guide with an overview of Day 2 and Day 4 content, including Colab links for notebooks.             | *(No executable code; provides course context and instructions for opening notebooks in Colab.)*                                                                                                                                                                                                                                                                                                                                             |

**Notes:** The Day 2 folder contains R notebooks that introduce querying a simulated EHR database (the Eunomia demo dataset) and an optional data-quality exercise with White Rabbit. The Day 4 folder includes a Python notebook demonstration and associated resources for using Generative Pre-trained Transformers (GPTs) to classify medications. Day 4’s materials come with prepared prompt files, config files, and Python scripts to facilitate batch processing with the OpenAI API.

## R Quick-Start

To run the R-based content (Day 2 materials), you can either use a local R environment or Google Colab with an R kernel. Follow the steps below to install required packages and execute each R script/notebook.

### Local Setup (R on Your Computer)

1. **Install R (and RStudio):** If not already installed, download and install R from CRAN (and RStudio Desktop for convenience). Ensure your R version is up-to-date on Windows, macOS, or Linux.

2. **Obtain the repository code:** Clone the EPID731 GitHub repository or download it as a ZIP, then open the `EPID731` project folder in RStudio or set it as your working directory in R.

3. **Install required R packages:** The Day 2 notebook will automatically attempt to install all needed packages, but you may install them in advance for a smoother experience. In an R console, run:

   ```r
   install.packages(c("rJava", "remotes", "dplyr", "lubridate", "knitr",  
                      "DatabaseConnector", "RSQLite", "SqlRender", "urltools", "checkmate"))
   remotes::install_github("ohdsi/Eunomia", ref = "v1.0.0")
   ```

   This installs core packages for data manipulation and database access (e.g. **dplyr**, **DatabaseConnector**, **Eunomia** for the example database). (The code above mirrors the setup steps in the Day 2 notebook, which may take a few minutes to complete in R.)

4. **Run the R scripts/notebooks:** You can execute the Day 2 notebook code in several ways:

   * **Using RStudio:** Open a new R Notebook or R script, copy in portions of the code from `EPID731_Accessing_EHR_Data.ipynb`, and run them step by step.  (Alternatively, use the **Terminal** in RStudio to launch Jupyter if you prefer the notebook interface.)
   * **Using Jupyter with IRkernel:** Install the IRkernel package in R and register it: `install.packages("IRkernel"); IRkernel::installspec()`. Then, start Jupyter Notebook, open the Day 2 `.ipynb` file, and proceed with the R kernel. This approach allows you to run the notebook natively as it was intended, with all R code chunks executing in order.

   Regardless of method, the R code will download the Eunomia demo database and demonstrate combining data via R and SQL. After installing packages and loading libraries, follow the comments in the code for the analysis steps. (If using RStudio, you can ignore Colab-specific instructions like “Save a copy to Drive”.)

### Google Colab (R Kernel)

1. **Open the notebook in Colab:** Click the Colab link for the Day 2 notebook (from the README or the table above) to open it in your browser. Once Colab launches, **save a copy** of the notebook to your own Google Drive (via **File > Save a copy in Drive**), so you can run and edit it. The original repository notebook will be read-only in Colab.

2. **Switch the runtime to R:** By default Colab uses a Python runtime. Change it to **R** by going to **Runtime > Change runtime type**, then selecting **R** as the language[^4]. This will start an R kernel (using the IRkernel backend) so that you can execute R code cells in the notebook.

3. **Install packages inside Colab:** Run the setup code cells at the top of the notebook to install and load packages. Colab’s R environment is clean each session, so the first code cell will install `rJava` and other libraries (this can take \~5 minutes). Once completed, the subsequent cells will load the libraries and proceed with the analysis.

4. **Execute the notebook cells:** Follow the notebook instructions, running each cell in order. The Day 2 notebook will:

   * Connect to the example **Eunomia** EHR database and list tables.
   * Demonstrate an R approach to filter patients with specific conditions and medications.
   * Demonstrate an equivalent approach using a single SQL query (via DatabaseConnector).
     As you run cells, observe the outputs (tables, messages, etc.) and ensure you get similar results as described in the notebook text.

5. **(Optional) White Rabbit tutorial:** If time permits, open the bonus notebook on White Rabbit in Colab and repeat the steps above. This notebook shows how to use **White Rabbit**, an OHDSI tool for scanning data quality. It may direct you to download the White Rabbit Java tool separately. Follow the instructions in the notebook to run a data scan and interpret the report. This step is optional, but it provides insight into assessing EHR data quality before database conversion to the OMOP Common Data Model (CDM).

## Python Bridge

Day 4 of the course introduces a **Python** workflow (using the OpenAI GPT API) alongside the R-based content. In practice, the R and Python parts of the workshop are run in separate notebooks/environments. However, it’s possible to “bridge” between R and Python if needed, so that the two languages can work together in a single environment. For example, one might retrieve or prep data in R and then call a Python script to leverage a machine learning library or, in this case, a GPT model API.

The **Python components** in this repository are primarily in the Day 4 folder: the GPT-based medication classification is implemented in a Jupyter notebook with Python, and utility scripts (`gpt_line_processor.py`, etc.) handle batch processing and API calls. These Python scripts load configuration files and prompt templates, then send requests to the OpenAI API. If you are running the analysis in Colab, the Day 4 notebook will clone the repo and use these scripts automatically.

For users who want to integrate Python into an R workflow, one approach is to call Python from R on the fly. For instance, you can use R’s system command to run a Python snippet or script:

```r
# In an R-based Colab notebook, you can install Python packages and run Python code:
system("pip install openai pandas configparser tiktoken")   # install Python dependencies
system('python -c "import openai; print(123)"')             # simple Python test (should print 123 if successful)
```

The code above, when executed in an R notebook, uses the R `system()` function to first install required Python libraries and then run a short Python command. This demonstrates that you can invoke Python from R to, say, call the OpenAI API after preparing data in R. (In more complex scenarios, you might write a Python script and call it similarly, or use R Markdown with Python code chunks.)

Another, more advanced bridging tool is the **`reticulate`** R package, which provides a seamless interface to call Python directly from R. Reticulate allows you to import Python modules and use them as if they were native R objects, effectively weaving both languages together[^5]. For example, using reticulate you could import the OpenAI Python library in R and call its functions without leaving the R session. This approach is powerful for advanced users who want a tight integration of R and Python in the same notebook or analysis pipeline. (For this workshop, using separate notebooks for R and Python is perfectly fine, but reticulate is a good option to be aware of for future projects.)

## Colab Setup Guide

When using Google Colab for this workshop, here are some handy setup tips:

* **Access the GitHub repo in Colab:** You can open notebooks directly from the GitHub repository. In Colab, go to **File > Open Notebook**, then select the **GitHub** tab. Enter the repository URL or name (FritscheLab/EPID731), and Colab will list the notebooks available in the repo. Choose the notebook (e.g. Day 2 or Day 4 notebook) to open it[^6]. (You may need to "Allow third-party cookies" for Colab to access GitHub.) This approach ensures you’re running the latest version of the workshop notebooks. Alternatively, use `!git clone` in a Colab cell to download the entire repo, especially if you need to access multiple files (the Day 4 notebook actually does this for you automatically).

* **Switch between R and Python runtimes:** Colab allows running either R or Python. To change the runtime language, go to **Runtime > Change runtime type**. For the Day 2 notebook, select **R** (this loads the R/IRkernel environment). For the Day 4 notebook, ensure the runtime is **Python 3**. You can only use one language at a time per notebook, but you can open multiple Colab notebooks simultaneously (one using R, another using Python) if you wish to work with both. This runtime switch is crucial — if you try to run R code in a Python runtime (or vice versa), you’ll get errors about unknown commands. Colab will remember your choice for the session (you might see “R” or “Py” next to the connected status).

* **Saving outputs to Google Drive:** Any files saved or created in the Colab session (e.g. results CSVs, images, etc.) will vanish once the session resets, unless you save them to a persistent storage. The simplest way is to **mount your Google Drive** in Colab. Click the **Drive** icon on the left sidebar (folder tab) and choose *Mount Drive*, or run the snippet:

  ```python
  from google.colab import drive
  drive.mount('/content/drive')
  ```

  After authenticating, your Google Drive will be available at `/content/drive/MyDrive`. You can save outputs there (e.g. `write.csv(my_data, "/content/drive/MyDrive/EPID731_results/data.csv")` in R, or use the Drive path in Python file writes). This ensures that any results or files you generate during the workshop are stored in your own Drive and persist beyond the Colab session. Additionally, remember to save copies of the notebooks themselves to Drive (as mentioned earlier), so your code edits are not lost. Colab notebooks saved in Drive can also be downloaded later or even saved back to GitHub if needed.

## Curated External Resources

Below is a list of authoritative external resources to supplement your learning. These references provide additional background on R, Python, Colab, and other tools used in EPID731, and can help reinforce the concepts from Day 2 and Day 4:

* **R for Data Science (2nd ed.)** – An open-access book by Hadley Wickham & Garrett Grolemund that covers R programming and data analysis using the tidyverse (highly relevant to Day 2’s R content) [^8].

* **The Python Tutorial** (official docs) – The Python Software Foundation’s beginner tutorial, which offers a guided introduction to Python’s syntax and features (useful if you need a refresher before diving into the Day 4 Python code) [^9].

* **How to use R in Google Colab** – Step-by-step tutorial (with examples) on configuring Colab to run R code using the IRkernel, and tips for using R and its packages in the Colab environment (mirrors the steps we took for Day 2) [^4].

* **OpenAI API – Python Quickstart Guide** – Documentation and examples for using OpenAI’s Python API. This resource explains how to set up API keys, install the OpenAI Python package, and make requests – helpful for understanding and extending the Day 4 GPT demo [^10].

* **WhiteRabbit for ETL design (OHDSI)** – Official documentation for the WhiteRabbit tool used in the Day 2 bonus notebook. It explains how WhiteRabbit scans source data and produces a data profile report, which provides context for the data quality assessment portion of the workshop [^11].

* **dplyr: A Grammar of Data Manipulation** – Official tidyverse documentation for **dplyr**, the R package heavily used in Day 2. It succinctly describes dplyr’s data manipulation verbs (filter, select, mutate, etc.) and includes examples, serving as a handy reference when working on EHR data wrangling [^12].

* **reticulate (R-Python interoperability) Cheat Sheet** – Posit’s cheat sheet for the reticulate package, summarizing how to call Python from R and vice versa. This is a great resource if you plan to integrate Python code into R projects (beyond what was covered in this workshop) [^5].

## Glossary

*Below is a glossary of domain-specific terms and functions encountered in the EPID731 materials:*

* **DatabaseConnector:** An R package (from OHDSI) that facilitates connecting to various database systems from R, used in Day 2 to execute SQL queries on the Eunomia example database.
* **dplyr:** A popular R package for data manipulation (part of the tidyverse) that provides a set of intuitive functions (verbs) for filtering, selecting, and transforming data frames.
* **EHR (Electronic Health Record):** Digital collection of patient health information. In this context, EHR data refers to clinical data (e.g. diagnoses, medications) used for analysis in the course.
* **Eunomia:** An R package providing a small **simulated** EHR database that mimics the OMOP CDM structure. It’s used in Day 2 as a self-contained example dataset (so participants can practice queries without needing a real hospital database).
* **Generative Pre-trained Transformer (GPT):** A type of large language model that generates human-like text by predicting words from training on vast datasets. In Day 4, GPT models (like GPT-3.5 or GPT-4 via OpenAI’s API) are used to classify medication entries.
* **Google Colab:** A free cloud-based Jupyter notebook service provided by Google. It allows users to run code (Python, R, etc.) in a web browser with no local setup, leveraging Google’s computing resources (including GPUs/TPUs).
* **IRkernel:** The R kernel for Jupyter notebooks. It enables running R code in Jupyter or Colab environments. (In Colab, selecting an R runtime launches an instance of IRkernel behind the scenes to execute R commands.)
* **Jupyter Notebook:** An interactive notebook interface that lets you combine executable code, formatted text, and outputs (tables, plots) in one document. Both the Day 2 and Day 4 materials are provided as Jupyter notebooks (for R and Python respectively).
* **OMOP CDM (Common Data Model):** A standardized data schema developed by the OHDSI community for observational health data. It defines common tables and fields for EHR data. Day 2’s White Rabbit tutorial and Eunomia dataset are set in the context of the OMOP CDM, preparing data for eventual use in this common format.
* **OpenAI API:** A cloud-based API provided by OpenAI that allows programs to interact with OpenAI’s models (such as GPT-3.5 and GPT-4) by sending requests with an authentication key. In Day 4, the OpenAI API is used to submit medication names to the GPT model and retrieve standardized classifications.
* **Prompt (GPT context):** Input text given to a GPT model to elicit a response. A *system prompt* defines context or instructions for the model (e.g. “You are a helpful assistant…”), while a *user prompt* is the actual query or task. Crafting effective prompts (“prompt engineering”) is key to getting useful model outputs.
* **reticulate:** An R package that provides a comprehensive set of tools for interoperability between R and Python. Reticulate allows you to call Python code from R, pass data between R and Python, and even import Python libraries into R as if they were R objects. It essentially “weaves together” the two languages in a single environment.
* **RStudio:** A popular integrated development environment (IDE) for R. It provides a user-friendly interface for writing R code, running analyses, and viewing results. (Note: RStudio is now part of Posit; the IDE may also be referred to as Posit Workbench.) Participants running code locally may use RStudio to edit and run the workshop scripts.
* **SQL (Structured Query Language):** A domain-specific language used to manage and query relational databases. In Day 2, SQL is used to directly query the Eunomia database (e.g. to find patients with certain conditions and medications) as an alternative to fetching the data into R and then filtering.
* **tidyverse:** An ecosystem of R packages for data science that share a common philosophy and design. The tidyverse includes packages like dplyr, ggplot2, tidyr, readr, etc., which are used for data manipulation, visualization, and more. The Day 2 materials use several tidyverse packages (dplyr for data manipulation, lubridate for dates, etc.) to work with EHR data in a fluent manner.
* **White Rabbit:** A data profiling tool from OHDSI used to examine the contents of an EHR database. White Rabbit scans tables and fields and produces a summary report of data characteristics (e.g. distinct values, frequency, etc.). In the workshop’s bonus material, White Rabbit is used to assess data quality and prepare for mapping the data to the OMOP CDM (often in conjunction with a tool called Rabbit-in-a-Hat for ETL planning).

## References

[^1]: FritscheLab – *EPID731 Day 2 Materials (README)* – GitHub Repository – 2023.

[^2]: FritscheLab – *EPID731 Day 4 Materials (README)* – GitHub Repository – 2023.

[^3]: FritscheLab – *EPID731\_Accessing\_EHR\_Data.ipynb* (Day 2 Notebook) – GitHub Repository – 2023.

[^4]: Bruno Ponne – *How to use R in Google Colab?* – codingthepast.com – 2023.

[^5]: RStudio – *reticulate: R Interface to Python* (Documentation) – rstudio.github.io – 2022.

[^6]: Stack Overflow – *How can I run notebooks of a Github project in Google Colab?* (Jaya Raghavendra answer) – 2021.

[^7]: Stack Overflow – *How to read data in Google Colab from Google Drive?* (Bob Smith answer) – 2020.

[^8]: Hadley Wickham & Garrett Grolemund – *R for Data Science (2nd Edition)* – [https://r4ds.hadley.nz](https://r4ds.hadley.nz) – 2023.

[^9]: Python Software Foundation – *The Python Tutorial* – [https://docs.python.org/3/tutorial](https://docs.python.org/3/tutorial) – 2023.

[^10]: GeeksforGeeks – *OpenAI Python API – Complete Guide* – [https://www.geeksforgeeks.org/data-science/openai-python-api/](https://www.geeksforgeeks.org/data-science/openai-python-api/) – 2025.

[^11]: OHDSI – *WhiteRabbit for ETL design* – [https://www.ohdsi.org/analytic-tools/whiterabbit-for-etl-design/](https://www.ohdsi.org/analytic-tools/whiterabbit-for-etl-design/) – 2025.

[^12]: Posit – *dplyr: A Grammar of Data Manipulation* (Documentation) – [https://dplyr.tidyverse.org](https://dplyr.tidyverse.org) – 2023.
