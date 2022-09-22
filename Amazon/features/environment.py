
def after_step(context, step):

    screenshot_route = "Amazon/resources/screenshots/"+ step.name + ".png"

    if step.status == "failed":
        context.driver.save_screenshot(screenshot_route)


