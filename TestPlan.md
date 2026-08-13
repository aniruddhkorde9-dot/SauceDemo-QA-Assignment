# Swag Labs Test Plan

**Tester:** Aniruddh Laxman Korde

## 1. Scope
Testing the main features of the Swag Labs shopping website. This includes logging in, looking at products, sorting items, adding things to the cart, and checking out.

## 2. Types of Testing
*   **Manual Testing:** Clicking around the website like a normal user to see if buttons, text boxes, and links actually work.
*   **Visual Testing:** Checking if the pictures and text look correct on the screen.
*   **Negative Testing:** Seeing what happens when things break or when the website doesn't act how it is supposed to.

## 3. Test Environment
*   **Operating System:** Windows 11
*   **Browser:** Google Chrome
*   **Device:** Desktop computer

## 4. Test Data
*   **Website:** https://www.saucedemo.com
*   **Test Username:** `problem_user`
*   **Test Password:** `secret_sauce`

## 5. Test Cases (Bug Reports)

### Bug 1: Wrong Product Pictures
*   **What is wrong:** Every single product on the main page shows the exact same picture of a dog.
*   **Severity:** High
*   **How to see it:**
    1. Go to `https://www.saucedemo.com`.
    2. Log in using `problem_user`.
    3. Look at the pictures of the items for sale.
*   **What should happen:** A backpack should show a picture of a backpack, a shirt should show a shirt, etc.
*   **What actually happens:** All items show a picture of a dog holding a tennis ball.

### Bug 2: Cannot Type Last Name at Checkout
*   **What is wrong:** The "Last Name" box at checkout is broken and forces your typing into the "First Name" box.
*   **Severity:** Critical 
*   **How to see it:**
    1. Log in as `problem_user`.
    2. Put something in the cart and go to the checkout screen.
    3. Click on the "Last Name" box and try to type your name.
*   **What should happen:** You should be able to type your full last name normally.
*   **What actually happens:** It only lets you type one letter, and it puts that letter into the "First Name" box instead. Because you can't fill out your last name, the website gives an error and blocks you from buying anything.

### Bug 3: Sorting Menu Does Not Work
*   **What is wrong:** The filter menu at the top right (A to Z, Price) is completely broken.
*   **Severity:** Medium/High 
*   **How to see it:**
    1. Log in as `problem_user` and go to the main products page.
    2. Click the sorting menu in the top right corner.
    3. Click on any option, like "Price (low to high)".
*   **What should happen:** The products should instantly rearrange themselves based on what you clicked.
*   **What actually happens:** Nothing happens at all. The products stay in the exact same order and the menu ignores your click.

### Bug 4: Broken "About" Link
*   **What is wrong:** Clicking the "About" link takes you to a dead page.
*   **Severity:** Medium 
*   **How to see it:**
    1. Log in as `problem_user`.
    2. Click the three lines in the top-left corner to open the side menu.
    3. Click on "About".
*   **What should happen:** It should take you to a real page with information about the Swag Labs company.
*   **What actually happens:** You get sent to a "404 - Page Not Found" error screen.

### Bug 5: Red "Remove" Button Does Nothing
*   **What is wrong:** The "Remove" button on the main products page does not actually take the item out of your cart.
*   **Severity:** High
*   **How to see it:**
    1. Log in as `problem_user`.
    2. Click "Add to cart" on any item. 
    3. The button will turn red and say "Remove". Click that red button.
*   **What should happen:** The item should be removed from your cart and the button should go back to saying "Add to cart".
*   **What actually happens:** The click is totally ignored. The item stays in your cart, and you have to physically go to the Cart page to remove it.

## 6. Summary of Issues
The biggest problem right now is Bug 2, because a customer physically cannot buy anything since the 'Last Name' box is broken. Also, seeing wrong pictures for every product makes the website look fake or broken. These major issues will frustrate users and need to be fixed before real customers try to use the site.