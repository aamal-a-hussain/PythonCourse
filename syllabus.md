# Weekend 1: Python Fundamentals

- Variables
- Arithmetic
- Control Flow (If, Fors, Whiles, Match)
- Functions (Arguments, Variable Scoping)
- Collections (Lists, Dictionary, Tuples)

For the below, first do given data, then do user input, then a for-loop, then read from file

Simple Arithmetic
    - Might be worth doing a simple banking app simulator here:
        - Take in expenses from a file
        - Categorise them
        - Create a savings pot and implement a round-up savings function
        - Predict returns over time based on interest.

Control Flow:
    - Blood Pressure Categorisation
    - Heart Rate
    https://www.kaggle.com/datasets/shayanfazeli/heartbeat/data

    - During this, we will also look at plotting data with matplotlib. (e.g. look at moving averages of data)
    - Take a list of 1000 voltage readings & plot them
    - find the maximum value
    - remove the drift caused by breathing (moving average)
    - find the slope of the signal
        - use it to detect the qrs
        - use that to get the heart rate

    - Image Segmentation (CXR)
        - Detect lung boundaries
        - Do some smoothing to get a better estimate of the edges
        - obtain Heart width and Thoracic Width


Mini-Project:
    Save the Patient ID, HR, CTR, and Priority Status to file



# Weekend 2: Object Oriented Programming

Extend the Patient database from the last one (which was dictionaries / csv) to a Patient Class
    - why is this useful? because we can add methods to the class

    As an example we can create a method which adds medication & vitals can be updated
    This can communicate with a server / frontend where a user can create their own patient profile, put in their vitals & check their medication.
        Students are required to create the necessary classes and methods.


Final Project: https://medshapenet.ikim.nrw/
    - We will have a pretrained 3d model that takes in a 3d scan of a skull with defects
        and outputs the coordinates of an implant that can fit that defect
        - the student will need to create a surgical plan that includes
            - The Patient id
            - The surgeon id
            - The skull obj

        - They will need to do some preprocessing on the skull object to pass it into the model
        - The model will output the implant

        - They will then need to check if the implant actually fits the hole

    - We can then create a bit of a surgical checklist based on patient medical history (e.g. comorbidities / medications, comparing volume of ai-generated implant to original bone fragment)

    Our frontend can display the skull & implant as well as a surgical checklist
        - We can make it so that the patient can see certain information if they login with their details & the surgeon can see other info if they login with their details
        - The student would have to create the logic to hide / show information.
