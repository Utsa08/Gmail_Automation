from selenium.webdriver.common.by import By


class AllLocators:
    #LoginPage
    emailID = (By.XPATH, "//input[@id='identifierId']")
    next1 = (By.XPATH, "//span[text()='Next']")
    password = (By.XPATH, "//input[@type='password']")
    next2 = (By.XPATH, "//span[text()='Next']")
    gmailImg =(By.XPATH,"//img[@role='presentation']")

    #ComposePage
    compose = (By.XPATH, "//div[contains(text(),'Compose')]")
    to = (By.XPATH, "//input[@aria-label='To recipients']")
    subject = (By.XPATH, "//input[@name='subjectbox']")
    description = (By.XPATH, "//div[@role='textbox']")
    send = (By.XPATH, "//div[@aria-label='Send ‪(Ctrl-Enter)‬']")
    messageSent = (By.XPATH,"//span[text()='Message sent']")

    #MessagePage
    sentButton = (By.XPATH,"//a[@aria-label='Sent']")
    anytime = (By.XPATH,"//span[text()='Any time']")
    messageSubject = (By.XPATH,"//td[@class='yX xY ']")
    text = (By.XPATH, "//div[contains(text(),'Python')]")

    #SearchPage
    search = (By.XPATH, "//input[@aria-label='Search mail']")
    searchButton = (By.CSS_SELECTOR, "button[aria-label='Search mail']")
    convo = (By.XPATH,"//div[text()='Conversations']")
    searchMessage = (By. XPATH,"//span[@class='bog']")
    desc = (By.XPATH, "//div[contains(text(),'Python')]")

    #LabelPage
    label = (By.XPATH, "//div[@aria-label='Create new label']")
    labelName = (By.XPATH, "//span//input[@type='text']")
    labelCreate = (By.XPATH, "//span[text()='Create']")
    labelCheck = (By.XPATH,"//label[contains(.,' already exists')]")

    #SettingsPage
    settings = (By.XPATH, "//a[@aria-label='Settings']")
    settingsRadioButton = (By.XPATH, "//div[text()='Compact']")
    settingsClose = (By.XPATH, "//div/button[@aria-label='Close']")

    #FilterPage
    filter = (By.XPATH, "//button[@aria-label='Advanced search options']")
    filterDate = (By.XPATH, "//div[@aria-label='Date within']")
    filterSelectDate = (By.XPATH, "//div[text()='3 days']")
    filterSearch = (By.XPATH, "//div[@aria-label='Search Mail']")
    filterAssert = (By.XPATH,"//div[text()='Conversations']")

    #DraftPage
    draft = (By.XPATH,"//a[normalize-space()='Drafts")
    draftDiv = (By.XPATH, "//td[contains(.,'don't have any saved drafts.')]")
    draftCheckbox = (By.XPATH,"(//span[@role='checkbox'])[2]")
    draftDiscard = (By.XPATH,"//div[contains(text(),'Discard')]")

    #TrashPage
    more = (By.XPATH, "(//span[@class='ait'])[1]")
    trash = (By.XPATH, "//a[@aria-label='Trash']")
    fromTrash = (By.XPATH, "//span[text()='From']")
    trashCheck=(By.XPATH,"//td[text()='No conversations in Trash.']")
    checkbox = (By.XPATH, "(//span[@role='checkbox'])[2]")
    delete = (By.XPATH, "//div[text()='Delete forever']")

    #LogoutPage
    profileIcon = (By.XPATH, "//a[contains(@aria-label, 'Google Account')]")

    #SpamPage
    spam = (By.XPATH,"//a[@aria-label='Spam']")
    spamCheck =(By.XPATH,"//td[contains(text(),'no spam')]")
