import "./Chat.css";
import checkIcon from "../assets/check.svg";

function Chat() {

  return (
    <>
        <div className="main-pane">
            <div className="chat-container">
                <div className="cc-header">
                    <div className="cc-header-title">
                        Chat
                    </div>
                    <div className="cc-header-subtitle">
                        Have a natural conversation in German
                    </div>
                </div>

                <div className="cc-chat">
                    <div className="cc-message-buddy">
                        <div className="cc-message-buddy-lable">Buddy</div>
                        <div className="cc-message-buddy-content">Hallo! Wie ghet es dir?</div>
                        <div className="cc-message-buddy-translation">Hi! How are you?</div>
                        <div className="cc-message-buddy-stats">
                            <div className="cc-message-buddy-time">00:00</div>
                            <div className="cc-message-buddy-send">
                                <img src={checkIcon} alt="check" />
                                <img src={checkIcon} alt="check" />
                            </div>
                        </div>
                    </div>
                    <div className="cc-message-user">
                        <div className="cc-message-user-lable">You</div>
                        <div className="cc-message-user-content">Ich bin gut und dir?</div>
                        <div className="cc-message-user-stats">
                            <div className="cc-message-user-time">00:00</div>
                            <div className="cc-message-user-send">
                                <img src={checkIcon} alt="check" />
                                <img src={checkIcon} alt="check" />
                            </div>
                        </div>
                    </div>
                </div>

                <div className="cc-io">
                    <div className="cc-io-type">
                        <input type="text" placeholder="Type your message in German" />
                    </div>
                    <div className="cc-io-record"></div>
                    <div className="cc-io-send"></div>
                </div>
            </div>
        </div>
    </>
  )
}

export default Chat
