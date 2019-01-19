import React from "react";

const Msg = ({when,p_num,id,filter,msg}) => {
  return (
    <div className="msg">
      <div className="message">{msg}</div>
        <div className="p_num">{p_num}</div>
        <div className="when">{when}</div>
      
    </div>
  );
};

export default Msg;
