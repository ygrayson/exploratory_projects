//
//  ViewController.swift
//  RL_Running_Man_Storyboard
//
//  Created by Qianbo Yin on 5/20/21.
//

import UIKit
import AVKit
import AVFoundation

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func playVideo(_ sender: UIButton) {
        // access to local video
        guard let path = Bundle.main.path(forResource: "agent", ofType:"mp4") else {
                debugPrint("video not found")
                return
            }
        // Create an AVPlayer, passing it the HTTP Live Streaming URL.
        let player = AVPlayer(url: URL(fileURLWithPath: path))

        // Create a new AVPlayerViewController and pass it a reference to the player.
        let controller = AVPlayerViewController()
        controller.player = player

        // Modally present the player and call the player's play() method when complete.
        present(controller, animated: true) {
            player.play()
        }
    }
}

