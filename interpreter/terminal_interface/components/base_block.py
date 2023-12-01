"""

A module providing a base class for creating interactive blocks that are displayed using the `rich` library's Live feature.

Classes:
    BaseBlock: A base class meant for extension, integrating the `rich.live.Live` class for
               creating live-updating terminal output.

Attributes:
    live (rich.live.Live): An instance of `Live` used to control live-updating terminal output.

Methods:
    __init__(self):
        Instantiates the `BaseBlock` object initializing the `Live` instance with
        specific configurations for display.

    update_from_message(self, message):
        Abstract method that subclasses must override to define how messages should update
        the block's display. It's called with a message that will carry data to
        reflect in the UI.

        Args:
            message: A data structure containing information to render in the UI.

        Raises:
            NotImplementedError: If a subclass does not implement this method.

    end(self):
        Finalizes the block's display by stopping the updating terminal output and
        possibly altering the cursor's visibility.

    refresh(self, cursor=True):
        Abstract method that must be implemented by subclasses to refresh the block's
        display in the terminal.

        Args:
            cursor (bool): A flag to determine whether to show the cursor when refreshing.

        Raises:
            NotImplementedError: If a subclass does not implement this method.

Note: Documentation automatically generated by https://undoc.ai
"""
from rich.console import Console
from rich.live import Live


class BaseBlock:
    """
        A class representing a base block for live updates in console output.
        This class serves as an abstract base class for objects that are intended to handle live updates. It initializes a `Live` object from the `rich.live` module which is used to manage live display of content in the console.
        Attributes:
            live: A `Live` instance used for managing live output in the console. It is set to not auto-refresh by default and handles the display of content with visible vertical overflow.
        Methods:
            __init__: Constructor to initialize the `Live` object.
            update_from_message: An abstract method that should be implemented by subclasses to update the live output based on a given message.
            end: Finalizes the output by refreshing it without the cursor and stopping the `Live` instance.
            refresh: An abstract method that should be implemented by subclasses to refresh the current live output, with an option to set visibility of the cursor.
        Raises:
            NotImplementedError: If `update_from_message` or `refresh` methods are called without being implemented in subclasses.
    """

    def __init__(self):
        """
        Initializes the live display for streaming output.
        This method sets up the live display with specified configurations. It initializes a Live object without
        auto refresh, a Console object for displaying output, and a vertical overflow setting. It also
        immediately starts the live display, making it ready for output streaming.
        Attributes:
            live (Live): An instance of the Live class that controls the live display. Auto refresh is
        disabled, and vertical overflow is set to 'visible'.
        """
        self.live = Live(
            auto_refresh=False, console=Console(), vertical_overflow="visible"
        )
        self.live.start()

    def update_from_message(self, message):
        """
        Raises:
            NotImplementedError: Always raised. Inherits from the Exception class.
        Description:
            This method serves as an abstract method which should be implemented by subclasses.
            It is intended to update the internal state of the instance based on the passed message.
            The method is deliberately not implemented, and it will raise a NotImplementedError
            if called directly, enforcing subclasses to provide a specific implementation.
            The exact behavior and parameters of the message will depend on the subclass implementation.
            This method is a placeholder in the base class and its signature or parameters
            are not defined here. It is the responsibility of the developer implementing the
            subclass to define the appropriate signature and behavior of the update_from_message
            method relevant to the subclass's context.
        """
        raise NotImplementedError("Subclasses must implement this method")

    def end(self):
        """
            Ends the display session for the live update mechanism.
            This method cleans up by refreshing the display without altering the cursor position
            and stops the live update functionality that was previously active.
        """
        self.refresh(cursor=False)
        self.live.stop()

    def refresh(self, cursor=True):
        """
            Raises:
                NotImplementedError: Always raised by this function to indicate that it
                    is intended to be overridden by subclasses.
            This function represents an interface in the base class that must be implemented
            by subclasses. When called, it simply raises a `NotImplementedError` to signify
            that the functionality has not been provided in the base class and must be
            supplied by the subclass. The particular method behavior will depend on the subclass
            implementation.
            Subclasses that inherit from this base class should provide their own implementation
            of this method to perform the necessary operations to refresh. For example, if this
            is a part of a user interface system, a subclass may implement this method to update
            the display or to refresh the cursor.
            Note that the `cursor` parameter is not utilized in the base class implementation
            and is present to dictate interface consistency across subclasses. Subclasses should
            pay attention to the `cursor` parameter if it is relevant to their refresh logic.
        """
        raise NotImplementedError("Subclasses must implement this method")
