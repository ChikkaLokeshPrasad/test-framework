"""
config/locators.py
------------------
Every selector for the app at:
  https://react-frontend-api-testing.vercel.app

All selectors were derived from the real app HTML.

LEARNING NOTE:
  Keeping locators here means:
  - Tests never contain CSS / XPath strings
  - One selector change = one-line fix
  - You can grep this file to find any locator instantly
"""
from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL            = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD         = (By.CSS_SELECTOR, "input[type='password']")
    SUBMIT           = (By.CSS_SELECTOR, "button[type='submit']")
    # Bootstrap alert rendered on bad credentials / validation
    ERROR_ALERT      = (By.CSS_SELECTOR, "div.alert")


class NavLocators:
    # Sidebar nav links
    ALL_NAV_LINKS    = (By.CSS_SELECTOR, "a.nav-link")
    # Currently-active page link has bg-primary class added by the app
    ACTIVE_LINK      = (By.CSS_SELECTOR, "a.bg-primary.nav-link")
    # Logout — Bootstrap nav item or button
    LOGOUT           = (By.CSS_SELECTOR, "a[href='/logout'], button[class*='logout']")
    # Logged-in user info shown in top navbar
    USER_INFO        = (By.CSS_SELECTOR, ".navbar .navbar-text, .navbar span.nav-link")


class DashboardLocators:
    HEADING          = (By.TAG_NAME, "h2.fw-bold")
    MAIN_CARD        = (By.CSS_SELECTOR, ".card, .container")


class UsersLocators:
    # Bootstrap warning alert shown to non-admin users
    ACCESS_DENIED    = (By.CSS_SELECTOR, "div.alert.alert-warning")
    # Admin sees a real users table
    TABLE            = (By.CSS_SELECTOR, "table")
    TABLE_ROWS       = (By.CSS_SELECTOR, "table tbody tr")
    # Nav link to Users page
    NAV_LINK         = (By.XPATH, "//a[contains(@class,'nav-link') and contains(text(),'User')]")


class ProjectsLocators:
    NEW_BTN       = (By.CSS_SELECTOR, "button.btn.btn-primary")
    MODAL         = (By.CSS_SELECTOR, ".modal.show, .modal-dialog")
    NAME_INPUT    = (By.CSS_SELECTOR, ".modal input.form-control")
    DESC_INPUT    = (By.CSS_SELECTOR, ".modal textarea.form-control")
    MODAL_SUBMIT  = (By.CSS_SELECTOR, ".modal button[type='submit']")
    STATUS_FILTER = (By.CSS_SELECTOR, "select.form-select")
    PROJECT_ITEMS = (By.CSS_SELECTOR, "table tbody tr")
    PROJECT_NAME  = (By.CSS_SELECTOR, "td:nth-child(2) .fw-semibold")
    SEARCH_INPUT  = (By.CSS_SELECTOR, "input[type='search']")


class TasksLocators:
    TABLE_ROWS    = (By.CSS_SELECTOR, "table tbody tr")
    STATUS_SELECT = (By.CSS_SELECTOR, "select.form-select, select[name='status']")
    STATUS_BADGE  = (By.CSS_SELECTOR, "td:nth-child(3) .badge")
    EDIT_BTN      = (By.CSS_SELECTOR, "button.btn-outline-primary.btn-sm")
    SAVE_BTN      = (By.CSS_SELECTOR, "button[type='submit'], button.btn-success")


class TestScenariosLocators:
    # ── Alerts & Dialogs (real IDs from the app HTML) ─────────────────────────
    ALERT_BTN        = (By.ID, "btn-simple-alert")
    CONFIRM_BTN      = (By.ID, "btn-confirm")
    PROMPT_BTN       = (By.ID, "btn-prompt")
    CONFIRM_RESULT   = (By.ID, "confirm-result")
    PROMPT_RESULT    = (By.ID, "prompt-result")

    # ── iFrame ────────────────────────────────────────────────────────────────
    IFRAME           = (By.CSS_SELECTOR, "iframe")
    IFRAME_BODY_TEXT = (By.CSS_SELECTOR, "body, p, h1, h2, div")

    # ── New Tab / Popup buttons ───────────────────────────────────────────────
    NEW_TAB_BTN      = (By.CSS_SELECTOR,
                        "button[id*='tab'], a[target='_blank'], button[class*='tab']")
    POPUP_BTN        = (By.CSS_SELECTOR,
                        "button[id*='popup'], button[id*='window']")
    # Heading of the Test Scenarios page itself
    PAGE_HEADING     = (By.CSS_SELECTOR, "h1, h2, .card-title")
