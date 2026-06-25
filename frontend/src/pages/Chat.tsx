import "./Chat.css";
import { useState } from "react";
import sendIcon from "../assets/send.svg";
import micIcon from "../assets/mic.svg";

function Chat() {
    const [chatFormText, setChatFormText] = useState('');

    function sendMessage() {
        if (!chatFormText.trim()) return;

        console.log(chatFormText);

        setChatFormText("");
    }

    function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault();
        sendMessage();
    }

    function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    }

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

                {/* <div className="cc-io">
                    <div className="cc-io-type">
                        <input type="text" placeholder="Type your message in German" />
                    </div>
                    <div className="cc-io-send">
                        <img src={micIcon} alt="mic"/>
                    </div>
                    <div className="cc-io-record">
                        <img src={sendIcon} alt="send"/>
                    </div>
                </div> */}

                <form className="cc-io" onSubmit={handleSubmit}>
                    <textarea
                        className="cc-io-type"
                        id="chatFormText"
                        placeholder="Write your message here..."
                        value={chatFormText}
                        onChange={(e) => setChatFormText(e.target.value)}
                        onKeyDown={handleKeyDown}
                    />
                    <button className="cc-io-send" type="submit">
                        <span className="material-symbols-outlined">arrow_upward</span>
                    </button>
                </form>
            </div>
        </div>
    </>
    )
}

export default Chat
