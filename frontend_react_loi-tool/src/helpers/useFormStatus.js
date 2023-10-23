// useFormStatus.js
import { useState } from 'react';

export default function useFormStatus() {

    const [formStatus, setFormStatus] = useState({'test': 'test'});
    var settingState = false
  
    function customSetStatus(key, value) {

        // Prevent setState calls inside the setter
        if (settingState) return;

        settingState = true;

        // Create new status object
        const newStatus = {...formStatus}; 
      
        // If key exists, update value
        if (key in newStatus) {
            newStatus[key] = value;
        } 
        // Otherwise add new key-value
        else {
            newStatus[key] = value;  
        }
      
        // Update state
        setFormStatus(newStatus);

        settingState = false;
      
    }
  
    return {
      formStatus,
      setFormStatus: customSetStatus 
    };
  
}