from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("""%Y-%m-%d %H_%M_%S""")

logs = []
instanceTime = formatted_datetime

def sys_LOG(message, type=None):
    """
    System logging, which logs to the console and a .txt file
    that contains all the logs from this instance.

    :param message: System log message
    :param type: what type of command (Optional)
    """
    if type == None:
        type = "Unspecified"
    log_output = (f"LOG | {formatted_datetime} - {type.upper()}: {message}\n")
    logs.append(log_output)

    with open(f"logs/SESSION_{instanceTime}.txt", "a", encoding="utf-16") as file:
        file.writelines(log_output)
    log_output = (f"LOG | {formatted_datetime} - {type.upper()}: {message}")
    print(log_output)