import "./Chat.css";
import checkIcon from "../assets/check.svg";
import sendIcon from "../assets/send.svg";
import micIcon from "../assets/mic.svg";

function Chat() {

  return (
    <>
        <div className="main-pane">
            <div className="chat-container">
                <div className="cc-chat">
                    <div className="cc-message buddy">
                        <div className="cc-message-buddy-content">Hallo! Wie ghet es dir?</div>
                        <div className="cc-message-buddy-translation">Hi! How are you?</div>
                    </div>
                    <div className="cc-message user">
                        <div className="cc-message-user-content">Ich bin gut und dir?</div>
                    </div>
                    <div className="cc-message buddy">
                        <div className="cc-message-buddy-content">Ich bien auch gut, Danke!</div>
                        <div className="cc-message-buddy-translation">I am fine too, thanks!</div>
                    </div>
                </div>

                <div className="cc-io">
                    <div className="cc-io-type">
                        <input type="text" placeholder="Type your message in German" />
                    </div>
                    <div className="cc-io-send">
                        <img src={micIcon} alt="mic"/>
                    </div>
                    <div className="cc-io-record">
                        <img src={sendIcon} alt="send"/>
                    </div>
                </div>
            </div>
        </div>
    </>
  )
}

export default Chat
