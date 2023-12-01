using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;


public class SceneChange : MonoBehaviour
{
    public string sceneName;

    // Update is called once per frame
    void Update()   
    {
        if(Input.GetKeyUp(KeyCode.C)){

            SceneManager.LoadScene(sceneName);  
        }
    }
}
