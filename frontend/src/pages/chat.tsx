import "./chat.css";
import userIcon from "../assets/user.svg";

function Chat() {

  return (
    <>
        <div className="chat-container">
            <div className="chat-side-pane">

                <div className="csd-header">
                    <div className="csd-header-icon">
                        GB
                    </div>
                    <div className="csd-header-title">
                        German AI Buddy
                    </div>
                </div>

                <div className="csd-nav">
                    <ul>
                        <li>New Conversation</li>
                        <li>Chat</li>
                        <li>History</li>
                        <li>Mistakes</li>
                        <li>Progress</li>
                        <li>Settings</li>
                    </ul>
                </div>   
                
                <div className="csd-user">
                    <div className="csd-user-image">
                        <img src={userIcon} alt="user picture" />
                    </div>
                    <div className="csd-user-name">
                        User
                    </div>
                    <div className="csd-user-level">
                        A2
                    </div>
                    <div className="csd-user-bar"></div>
                </div>

            </div>

            <div className="chat-main-pane">

                <div className="cmp-header">
                    <div className="cmp-header-title">
                        Chat
                    </div>
                    <div className="cmp-header-subtitle">
                        Have a natural conversation in German
                    </div>
                </div>

                <div className="cmp-chat">
                    <div className="cmp-message-buddy">
                        <div className="cmp-message-buddy-lable">Buddy</div>
                        <div className="cmp-message-buddy-content">Hallo! Wie ghet es dir?</div>
                        <div className="cmp-message-buddy-translation">Hi! How are you?</div>
                        <div className="cmp-message-buddy-stats">
                            <div className="cmp-message-buddy-time">00:00</div>
                            <div className="cmp-message-buddy-send"></div>
                        </div>
                    </div>
                    <div className="cmp-message-user">
                        <div className="cmp-message-user-lable">You</div>
                        <div className="cmp-message-user-content">Ich bin gut und dir?</div>
                        <div className="cmp-message-user-stats">
                            <div className="cmp-message-user-time">00:00</div>
                            <div className="cmp-message-user-send"></div>
                        </div>
                    </div>
                </div>

                <div className="cmp-io">
                    <div className="cmp-io-type">
                        <input type="text" placeholder="Type your message in German" />
                    </div>
                    <div className="cmp-io-record"></div>
                    <div className="cmp-io-send"></div>
                </div>

            </div>
        </div>
    </>
  )
}

export default Chat
