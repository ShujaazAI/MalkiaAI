<img src="https://github.com/aceta-minophen/Rudra/blob/website/Website/public/Rudra.svg" align="right" width="200">

# Rudra
A smart healthcare assistant robot intended for home and hospital use.

> 🔍 **How to navigate this repository?**
> 
> The implementation of each feature has been explained in the [features](https://github.com/aceta-minophen/Rudra/edit/main/README.md#feet-features) section below along with the link to the respective folders of code files provided, explaining the contents in them. 
>
> Further, there are separate README files in each directory to elaborate on the purpose of the subfiles, etc.

## 🪶 Features
### 1. Voice Assistant 
> Often, the elderly are socially isolated, and many exist within the confines of a nursing home or an institution, where their main social links are only with other inmates and equally alienated old people. <sup>[[1]](https://github.com/aceta-minophen/Rudra/edit/main/README.md#-references)</sup>

Rudra's main goal is to interact with the elderly and keep them engaged. This will vastly help uplift their mental health, allow them to keep up with the times while also having someone to reminisce about the olden days with. Besides that, the family members won't feel burdened with their already busy lives, and can rest knowing the elderly are being well taken care of.

#### 1.1. Implementation

Rudra is a fully voice-operated, completely hands-free system for the elderly, so all they have to do is talk to Rudra to get a job done.

The voice assistant has been specially curated according to the needs of the elderly. It performs timely check ups on them, allows them to create reminders for themselves, listen to stories, call up any family members, and have a sympathic discussion on any topic they desire with the robot.

All this is accomplished by employing the following:
1. **NLP**: Natural language processing helps in discerning the tone and context of any spoken sentence, allowing Rudra to have more sympathetic reactions to it. **DialogFlow** has been used for this purpose.
2. **Expression-wise response**: Rudra continuously monitors the elderly's expressions to further improve the user's experience. This also helps in monitoring their mental health regularly.
3. **Query response**: Several API's have been used for providing the best one-shop-stop solution for any miscellanious queries the user might have. The API's are:
    1. Dialogflow
    2. Firebase Realtime Database
    3. Google Calendar
    4. [News](https://newsapi.org/)
    5. [Weather](https://openweathermap.org/api)
4. **Meal suggestion and reminders**: Physical wellbeing is equally as important as mental health, therefore, Rudra is designed to timely remind the elderly to drink water, have food and take any medicines if needed.
5. **Action Recognition**: Computer vision is used to make sure that the elderly has drunk water, had food and slept properly. The data is only updated in the backend once Rudra detects the above stated actions and then confirms them with the user to avoid misinterpretation.

#### 1.2. Working
- The code for the voice assistant is hosted on the Raspberry Pi.
- The voice input and output is taken and given through bluetooth headset connected to the Raspberry Pi. This helps eliminate any background noise. If multiple people are talking at once, Rudra will only hear the designated elderly speak.
- Every time that the elderly wants to initiate a conversation, they can do so by simply using the wakeword: "Hey, Rudra".
- The voice output can also be given using speakers connect to the Raspberry Pi, if the user wishes it so.

#### 1.3. Backend
Since Rudra works with a lot of different modules where data needs to be collected from different sensors and devices, **Firebase Realtime Database** is used to integrate all these separate nodes. Any data of food, water or medicine intake is committed to the database, along with important information regarding the elserly's current mood and other statements for future reference to further optimize the assistant's replies.

### 2. Human Following
### 3. Remote Control and Monitoring
### 4. Computer Vision
### 5. Physical Design
#### 5.1. Components
| Component  | Amount  | Utility |
|---| :-: |---|
| Raspberry Pi 4B | x1 | Microprocessor: running ROS and other code files |
| Motor Driver | x1 | Controlling the motors |
| BO Motors + wheels | x2 | Moving the robot |

#### 5.2. Design Specs
- Height:
- Weight:
- Speed:

## 📑Important Documents
### 1. Architecture / Flow Chart
### 2. App Wireframe
### 3. Cost Report
### 4. Business Plan
### 5. Demo Video

## 🔭 Features Under Construction
### 1. Guidance
### 2. Personality
### 3. Multi-bot control
### 4. Design
### 5. Website

## 🧩 About Us
### 1. 🍃 Srishti Agrawal
- **Role:** Team Leader
- **Contributions:**
- **Contact Me:** 
### 2. 🩹 Sukritee Sharma
- **Role:** Team Member
- **Contributions:**
- **Contact Me:** 
### 3. 🌂 Manasvvi Aggarwal
- **Role:** Team Member
- **Contributions:**
- **Contact Me:** 
### 4. 🫐 Utkarsha Kumari
- **Role:** Team Member
- **Contributions:**
- **Contact Me:** 
### 5. 🌮 Chandana Kunatala
- **Role:** Team Member
- **Contributions:**
- **Contact Me:** 
### 6. 🛰️ Sristi
- **Role:** Team Member
- **Contributions:**
- **Contact Me:** 
### 7. 🔖 Manvika Gupta
- **Role:** Team Member
- **Contributions:**
- **Contact Me:** 


## 📕 References
1. Parkar SR. Elderly mental health: needs. Mens Sana Monogr. 2015 Jan-Dec;13(1):91-9. doi: 10.4103/0973-1229.153311. PMID: 25838727; PMCID: PMC4381326.
