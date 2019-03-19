import MaxPlus


# ------------------------------------------------------------------------------
def set_current(frame):
    """
    Sets the current frame

    :param frame: 
    :return: 
    """
    MaxPlus.Animation.SetTime(frame * MaxPlus.Animation.GetTicksPerFrame())


# ------------------------------------------------------------------------------
def start():
    ticks = MaxPlus.Animation.GetTicksPerFrame()
    start_tick = MaxPlus.Animation.GetStartTime()
    start_frame = start_tick / ticks

    return start_frame


# ------------------------------------------------------------------------------
def set_start(frame):
    MaxPlus.Animation.SetRange(
        MaxPlus.Interval(
            frame * MaxPlus.Animation.GetTicksPerFrame(),
            MaxPlus.Animation.GetEndTime(),
        ),
    )


# ------------------------------------------------------------------------------
def end():
    ticks = MaxPlus.Animation.GetTicksPerFrame()
    end_tick = MaxPlus.Animation.GetEndTime()
    end_frame = end_tick / ticks

    return end_frame


# ------------------------------------------------------------------------------
def set_end(frame):
    MaxPlus.Animation.SetRange(
        MaxPlus.Interval(
            MaxPlus.Animation.GetStartTime(),
            frame * MaxPlus.Animation.GetTicksPerFrame(),
        ),
    )


def framerate():
    return None

