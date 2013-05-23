Live coding GLSL shaders with IPython
#####################################
:date: 2013-05-23 12:59
:category: Live Coding
:slug: live-coding-glsl-shaders-with-ipython

.. raw:: html

   <iframe width="560" height="315" src="http://www.youtube.com/embed/4iwQAqgG1uI" frameborder="0" allowfullscreen></iframe>

I recently started to learn some OpenGL and was looking for a nice way to use
Python for this. I wanted to be able to update the shaders quickly so that I
can quickly try out different code. This is one of the results. I was heavily
inspired by the live coding video of onomo.jp, in fact I practically copied
and adapted his code to get a start:

http://vimeo.com/51993089

The ideas and code of Cyrille Rossant was also very helpful, to get a start
with OpenGL in Python and IPython:

http://cyrille.rossant.net/2d-graphics-rendering-tutorial-with-pyopengl/

To get a start you can just run my gl_livecode.py script that I also use in
the beginning of the video. It is available as gist:

https://gist.github.com/pbouda/5531821

To process the audio I just split the stream in two frequency bins, more or less
randomly. I didn't rely on anything sophisticated but just used what gave the
most beautiful visualization in the end. The update function currently looks
like this::

	def move_stuff(self):
	    a = self.stream.read(chunk)
	    indata = np.array(wave.struct.unpack("%dh"%(chunk), a))*self.window
	    fft_data = abs(np.fft.rfft(indata))
	    total_sum = np.sum(fft_data)
	    spec_x = np.sum(fft_data[40:100])/(len(fft_data[40:100])*chunk*2048)
	    spec_y = np.sum(fft_data[250:])/(len(fft_data[250:])*chunk*32)
	    gl.glUniform2f(self.spec, spec_x, spec_y)

You can easily change the `move_stuff` function while the programm is running,
just use something like this in IPython::

	def move_stuff(self):
	    a = self.stream.read(chunk)
	    indata = np.array(wave.struct.unpack("%dh"%(chunk), a))*self.window
	    fft_data = abs(np.fft.rfft(indata))
	    total_sum = np.sum(fft_data)
	    spec_x = np.sum(fft_data[:220])/(len(fft_data[:220])*chunk*2048)
	    spec_y = np.sum(fft_data[220:])/(len(fft_data[220:])*chunk*32)
	    gl.glUniform2f(self.spec, spec_x, spec_y)
	f_move = types.MethodType(move_stuff, win.widget, GLPlotWidget)    
	win.widget.move_stuff = f_mov

This example changes the location and the size of the two frequency bins. To
update the fragment shader for example::

	FS = """#version 330
	uniform vec2 resolution;
	uniform vec2 spec;
	uniform float time;

	void main(void) {
	  vec2 uv = 2.0 * (gl_FragCoord.xy / resolution) - 1.0;
	  float col = 0.0;
	  //uv = abs(uv);
	  for (float i = 1.0; i<23.0; i++) {
	      uv.y += sin(i*20.0 + spec.x*5.0 + time*6.0 + uv.x*.5) * spec.y*2.5;
	      col += abs((.5*spec.x)/uv.y) * spec.y;
	  }
	  gl_FragColor = vec4(col,col,col,1.0);
	}
	"""
	win.widget.fs = FS
	win.widget.link_shaders()
	win.widget.get_uniforms()

Then iterate. :-) Have fun!